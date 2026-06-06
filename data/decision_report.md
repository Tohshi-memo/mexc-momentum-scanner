# Decision Report

- generated_at: 2026-06-06T14:55:58.212911+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5850**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5850, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.86% | **-1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.19% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.00% | **+3.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.78% | **+2.22%** |
| ASK_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.23% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$99.50** / 初期 $100.00 (-0.50%)
- 確定トレード: 1件 (TP 0 / SL 1 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1397件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T14:55:50.316837+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=60888.0
- Funnel: target 771 → liquid 144 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +113.21% | $71,908,584.10 |
| HEI/USDT:USDT | +77.31% | $4,351,342.69 |
| VELVET/USDT:USDT | +49.42% | $3,842,068.72 |
| BLUAI/USDT:USDT | +41.81% | $5,795,016.19 |
| CLO/USDT:USDT | +29.35% | $2,529,082.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +4.78% | +4.60% |
| BEAT/USDT:USDT | below_1h_threshold | +4.49% | +4.31% |
| ZEST/USDT:USDT | below_1h_threshold | +3.89% | +3.71% |
| EPIC/USDT:USDT | below_1h_threshold | +2.87% | +2.69% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.63% | +2.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
