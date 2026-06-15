# Decision Report

- generated_at: 2026-06-15T04:52:27.782943+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6745**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6745, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.53% | **+0.50%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| ASK | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.45% | **+1.09%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +1.56% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.16** / 初期 $100.00 (+72.16%)
- 確定: 1618件 (Win 423 / Loss 503 / Flat 692) / skip 1688件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $172.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.84** / 初期 $100.00 (-0.16%)
- 確定: 112件 (Win 24 / Loss 18 / Flat 70) / skip 44件
- 成長率目線: 平均log -0.000014 / 幾何平均 -0.001% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0654 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $99.84

## 5. Latest Market Context

- 更新: 2026-06-15T04:52:19.908713+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=65646.4
- Funnel: target 770 → liquid 144 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.7 >= 65=1, 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +128.49% | $2,565,512.23 |
| EVAA/USDT:USDT | +71.34% | $19,345,259.60 |
| CLO/USDT:USDT | +36.30% | $2,104,843.37 |
| WLD/USDT:USDT | +19.91% | $106,403,335.52 |
| GRASS/USDT:USDT | +17.98% | $1,356,002.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +3.74% | +4.12% |
| NIL/USDT:USDT | below_1h_threshold | +2.75% | +3.13% |
| BABY/USDT:USDT | below_1h_threshold | +2.75% | +3.12% |
| JTO/USDT:USDT | below_1h_threshold | +2.71% | +3.08% |
| NEAR/USDT:USDT | below_1h_threshold | +2.59% | +2.96% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
