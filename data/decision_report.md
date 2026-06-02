# Decision Report

- generated_at: 2026-06-02T06:57:12.158208+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5416**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5416, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.08% | **+0.46%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.20% | **+1.98%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.32% | **+1.62%** |
| ASK_LONG | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.00** / 初期 $100.00 (+37.00%)
- 確定: 928件 (Win 219 / Loss 275 / Flat 434) / skip 1049件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $137.00

## 4. Latest Market Context

- 更新: 2026-06-02T06:57:09.127163+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=69948.6
- Funnel: target 777 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 80.7 >= 65=1, 4h RSI 70.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +62.56% | $11,900,532.80 |
| US/USDT:USDT | +39.64% | $1,179,488.92 |
| ESPORTS/USDT:USDT | +27.38% | $11,986,266.08 |
| OPG/USDT:USDT | +20.84% | $1,124,828.28 |
| LAB/USDT:USDT | +20.12% | $219,258,494.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPG/USDT:USDT | below_1h_threshold | +3.34% | +3.75% |
| BSB/USDT:USDT | below_1h_threshold | +3.28% | +3.69% |
| UB/USDT:USDT | below_1h_threshold | +2.84% | +3.25% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.69% | +3.10% |
| CHIP/USDT:USDT | below_1h_threshold | +2.49% | +2.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
