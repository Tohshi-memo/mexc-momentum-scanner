# Decision Report

- generated_at: 2026-06-09T04:52:31.889848+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6114**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=6114, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.73% | **+0.58%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.72% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.66% | **+0.30%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.37% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 10件 (TP 1 / SL 8 / EXP 1)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.47** / 初期 $100.00 (+53.47%)
- 確定: 1154件 (Win 286 / Loss 354 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $153.47

## 4. Latest Market Context

- 更新: 2026-06-09T04:52:28.983495+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=63227.2
- Funnel: target 777 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +52.13% | $24,194,852.60 |
| SLX/USDT:USDT | +13.96% | $1,277,757.53 |
| CTR/USDT:USDT | +12.34% | $1,120,665.10 |
| POWER/USDT:USDT | +11.57% | $1,081,968.95 |
| MOVE/USDT:USDT | +8.99% | $5,639,716.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_relative_strength | +5.03% | +4.42% |
| UAI/USDT:USDT | below_1h_threshold | +3.52% | +2.91% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.43% | +2.81% |
| WLD/USDT:USDT | below_1h_threshold | +3.16% | +2.54% |
| UB/USDT:USDT | below_1h_threshold | +2.82% | +2.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
