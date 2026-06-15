# Decision Report

- generated_at: 2026-06-15T04:20:11.167585+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6740**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6740, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.58% | **+0.55%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +2.60% | **+0.52%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.02** / 初期 $100.00 (+73.02%)
- 確定: 1613件 (Win 423 / Loss 502 / Flat 688) / skip 1688件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $173.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.19** / 初期 $100.00 (+0.19%)
- 確定: 107件 (Win 24 / Loss 17 / Flat 66) / skip 44件
- 成長率目線: 平均log +0.000018 / 幾何平均 +0.002% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0634 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.19

## 5. Latest Market Context

- 更新: 2026-06-15T04:20:06.933510+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=65745.6
- Funnel: target 770 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +144.05% | $2,153,494.44 |
| EVAA/USDT:USDT | +62.39% | $18,755,390.13 |
| CLO/USDT:USDT | +32.34% | $2,071,851.44 |
| RIF/USDT:USDT | +32.20% | $4,924,830.46 |
| WLD/USDT:USDT | +19.79% | $102,886,209.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +3.67% | +3.89% |
| NIL/USDT:USDT | below_1h_threshold | +3.12% | +3.34% |
| EVAA/USDT:USDT | below_1h_threshold | +3.11% | +3.33% |
| CHIP/USDT:USDT | below_1h_threshold | +2.08% | +2.30% |
| LAB/USDT:USDT | below_1h_threshold | +1.88% | +2.10% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
