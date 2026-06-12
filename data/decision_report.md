# Decision Report

- generated_at: 2026-06-12T16:41:29.782141+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6524**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.56% / filled 20/20。**
- 全期間 MARKET基準: n=6524, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.80% | **+0.44%** |
| ASK | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.65% | **+1.82%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$95.16** / 初期 $100.00 (-4.84%)
- 確定トレード: 20件 (TP 3 / SL 16 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.67** / 初期 $100.00 (+64.67%)
- 確定: 1397件 (Win 385 / Loss 456 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $164.67

## 4. Latest Market Context

- 更新: 2026-06-12T16:41:22.850163+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.61% price=63948.9
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +14.08% | $174,272,363.92 |
| ESPORTS/USDT:USDT | +10.28% | $66,050,019.06 |
| BTW/USDT:USDT | +9.62% | $2,833,183.40 |
| RKLBSTOCK/USDT:USDT | +7.36% | $1,382,978.94 |
| PLAY/USDT:USDT | +5.45% | $5,785,587.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_relative_strength | +5.46% | +4.84% |
| COAI/USDT:USDT | below_relative_strength | +5.30% | +4.68% |
| SOXL/USDT:USDT | below_1h_threshold | +3.93% | +3.31% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +3.83% | +3.21% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +3.40% | +2.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
