# Decision Report

- generated_at: 2026-06-08T05:11:42.120629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6032**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.20% / filled 20/20。**
- 全期間 MARKET基準: n=6032, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |
| ASK | 20/20 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.78% | **+1.60%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.25% | **+0.81%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.60% | **+0.33%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.34% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.58** / 初期 $100.00 (-1.42%)
- 確定トレード: 7件 (TP 1 / SL 5 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1449件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T05:11:39.627557+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62650.7
- Funnel: target 773 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +37.30% | $97,482,287.75 |
| PIPPIN/USDT:USDT | +23.15% | $7,610,703.85 |
| ALLO/USDT:USDT | +21.96% | $37,306,845.48 |
| BLESS/USDT:USDT | +14.61% | $8,545,861.75 |
| VELVET/USDT:USDT | +14.31% | $3,231,672.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +1.30% | +1.30% |
| LUNC/USDT:USDT | below_1h_threshold | +1.28% | +1.28% |
| BEAT/USDT:USDT | below_1h_threshold | +1.26% | +1.27% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.13% | +1.14% |
| BLESS/USDT:USDT | below_1h_threshold | +1.12% | +1.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
