# Decision Report

- generated_at: 2026-06-09T15:42:03.537555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6145**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=6145, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.94% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.98% | **+0.30%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.49% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.25** / 初期 $100.00 (+50.25%)
- 確定: 1185件 (Win 297 / Loss 371 / Flat 517) / skip 1521件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.92% 残高後 $150.25

## 4. Latest Market Context

- 更新: 2026-06-09T15:42:00.189069+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=61314.1
- Funnel: target 774 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +35.04% | $6,259,056.31 |
| ESPORTS/USDT:USDT | +34.20% | $24,721,536.06 |
| JCT/USDT:USDT | +33.02% | $2,022,524.08 |
| POWER/USDT:USDT | +27.73% | $4,964,484.81 |
| PLAY/USDT:USDT | +20.34% | $2,751,239.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +4.71% | +5.03% |
| JCT/USDT:USDT | below_1h_threshold | +3.95% | +4.27% |
| CHIP/USDT:USDT | below_1h_threshold | +3.19% | +3.51% |
| ATOM/USDT:USDT | below_1h_threshold | +2.41% | +2.73% |
| BEAT/USDT:USDT | below_1h_threshold | +2.33% | +2.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
