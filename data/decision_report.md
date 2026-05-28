# Decision Report

- generated_at: 2026-05-28T16:19:50.191460+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4973**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4973, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.39% | **+0.83%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.10% | **+0.10%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +2.24% | **+1.99%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.93%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.69** / 初期 $100.00 (+28.69%)
- 確定: 708件 (Win 174 / Loss 221 / Flat 313) / skip 826件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDSSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.69

## 4. Latest Market Context

- 更新: 2026-05-28T16:19:47.548308+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=73099.4
- Funnel: target 776 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +5.58% | $1,416,236.29 |
| ESPORTS/USDT:USDT | +5.54% | $5,963,957.87 |
| SWARMS/USDT:USDT | +4.49% | $1,105,296.70 |
| ETHFI/USDT:USDT | +2.25% | $3,085,483.37 |
| H/USDT:USDT | +2.14% | $6,710,843.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SWARMS/USDT:USDT | below_1h_threshold | +4.49% | +4.22% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.25% | +1.98% |
| H/USDT:USDT | below_1h_threshold | +2.09% | +1.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.97% | +1.70% |
| NIL/USDT:USDT | below_1h_threshold | +1.85% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
