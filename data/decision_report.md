# Decision Report

- generated_at: 2026-06-11T20:30:28.441475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6403**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6403, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.09% | **+0.27%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_8PCT | 3/20 | 15.0% | -1.43% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.62% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.93** / 初期 $100.00 (+54.93%)
- 確定: 1320件 (Win 344 / Loss 421 / Flat 555) / skip 1644件
- 成長率目線: 平均log +0.000332 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $154.93

## 4. Latest Market Context

- 更新: 2026-06-11T20:30:24.776318+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=63340.8
- Funnel: target 782 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.4 >= 65=1, 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +95.80% | $114,915,867.86 |
| ESPORTS/USDT:USDT | +46.47% | $14,364,711.52 |
| NAORIS/USDT:USDT | +24.38% | $1,174,807.96 |
| UB/USDT:USDT | +16.89% | $1,651,867.92 |
| SKYAI/USDT:USDT | +11.20% | $12,364,952.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.47% | +3.83% |
| UB/USDT:USDT | below_1h_threshold | +3.42% | +3.79% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.38% | +2.75% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.38% | +2.74% |
| BEAT/USDT:USDT | below_1h_threshold | +2.29% | +2.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
