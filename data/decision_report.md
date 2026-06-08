# Decision Report

- generated_at: 2026-06-08T04:42:36.496567+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6029**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=6029, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.85% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.44%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$98.58** / 初期 $100.00 (-1.42%)
- 確定トレード: 7件 (TP 1 / SL 5 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.97** / 初期 $100.00 (+51.97%)
- 確定: 1143件 (Win 280 / Loss 349 / Flat 514) / skip 1447件
- 成長率目線: 平均log +0.000366 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $151.97

## 4. Latest Market Context

- 更新: 2026-06-08T04:42:30.494351+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.61% price=62715.8
- Funnel: target 773 → liquid 140 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.5 >= 65=1, 4h RSI 89.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +33.39% | $96,862,030.61 |
| ALLO/USDT:USDT | +23.83% | $42,645,158.78 |
| PIPPIN/USDT:USDT | +21.36% | $7,413,512.04 |
| BLESS/USDT:USDT | +16.96% | $8,619,099.90 |
| VELVET/USDT:USDT | +14.29% | $3,247,183.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.69% | +3.30% |
| LUNC/USDT:USDT | below_1h_threshold | +1.92% | +2.53% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.78% | +1.39% |
| USOIL/USDT:USDT | below_1h_threshold | +0.76% | +1.37% |
| CTR/USDT:USDT | below_1h_threshold | +0.13% | +0.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
