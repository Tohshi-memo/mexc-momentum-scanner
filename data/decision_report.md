# Decision Report

- generated_at: 2026-06-08T05:00:28.561111+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6031**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.60% / filled 20/20。**
- 全期間 MARKET基準: n=6031, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.11% | **+1.00%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.48% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.38%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.18% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$98.58** / 初期 $100.00 (-1.42%)
- 確定トレード: 7件 (TP 1 / SL 5 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1448件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T05:00:25.571794+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=62681.9
- Funnel: target 773 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +36.24% | $96,422,209.60 |
| ALLO/USDT:USDT | +22.00% | $36,876,100.33 |
| PIPPIN/USDT:USDT | +21.50% | $7,497,621.52 |
| VELVET/USDT:USDT | +13.94% | $3,222,204.95 |
| BLESS/USDT:USDT | +13.41% | $8,529,141.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +0.29% | +0.25% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.20% | +0.16% |
| HYPE/USDT:USDT | below_1h_threshold | +0.19% | +0.15% |
| EWY/USDT:USDT | below_1h_threshold | +0.19% | +0.14% |
| BEAT/USDT:USDT | below_1h_threshold | +0.15% | +0.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
