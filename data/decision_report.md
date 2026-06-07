# Decision Report

- generated_at: 2026-06-07T22:27:16.759057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6004**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6004, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +1.84% | **+0.46%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.89% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.16% | **+3.16%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.28% | **+1.71%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.27% | **+1.02%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.88% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.23** / 初期 $100.00 (+54.23%)
- 確定: 1121件 (Win 274 / Loss 338 / Flat 509) / skip 1444件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $154.23

## 4. Latest Market Context

- 更新: 2026-06-07T22:27:13.643648+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.07% price=63033.4
- Funnel: target 768 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +26.69% | $3,949,701.46 |
| BEAT/USDT:USDT | +25.78% | $74,844,711.04 |
| BTW/USDT:USDT | +22.71% | $13,920,879.29 |
| PIPPIN/USDT:USDT | +18.05% | $3,851,119.72 |
| BLESS/USDT:USDT | +14.86% | $8,267,883.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_relative_strength | +6.87% | +4.80% |
| PIPPIN/USDT:USDT | below_relative_strength | +5.30% | +3.23% |
| ZEC/USDT:USDT | below_1h_threshold | +4.82% | +2.75% |
| MYX/USDT:USDT | below_1h_threshold | +4.48% | +2.41% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +4.30% | +2.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
