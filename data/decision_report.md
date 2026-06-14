# Decision Report

- generated_at: 2026-06-14T17:54:20.968718+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6688**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=6688, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.81% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.53% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.76** / 初期 $100.00 (+73.76%)
- 確定: 1561件 (Win 417 / Loss 495 / Flat 649) / skip 1688件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $173.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.77** / 初期 $100.00 (-1.23%)
- 確定: 68件 (Win 19 / Loss 14 / Flat 35) / skip 31件
- 成長率目線: 平均log -0.000183 / 幾何平均 -0.018% per trade / maxDD +2.00%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0361 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.77

## 5. Latest Market Context

- 更新: 2026-06-14T17:54:16.761914+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=63740.0
- Funnel: target 770 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +18.04% | $3,143,203.57 |
| BANANAS31/USDT:USDT | +5.98% | $2,090,390.60 |
| CLO/USDT:USDT | +5.23% | $1,428,538.37 |
| STG/USDT:USDT | +4.81% | $6,577,073.00 |
| EDGE/USDT:USDT | +4.30% | $1,138,930.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.85% | +3.13% |
| EDGE/USDT:USDT | below_1h_threshold | +2.70% | +2.97% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.27% | +2.54% |
| MITO/USDT:USDT | below_1h_threshold | +2.17% | +2.44% |
| ALLO/USDT:USDT | below_1h_threshold | +1.54% | +1.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
