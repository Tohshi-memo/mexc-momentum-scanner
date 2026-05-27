# Decision Report

- generated_at: 2026-05-27T09:44:30.630891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4924**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=4924, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.23% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.79%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.39% | **+0.77%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.35% | **+0.26%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 801件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T09:44:26.171816+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=75892.6
- Funnel: target 775 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +22.06% | $15,013,815.60 |
| ALT/USDT:USDT | +17.12% | $1,191,775.98 |
| BEAT/USDT:USDT | +14.19% | $13,628,330.11 |
| LUNC/USDT:USDT | +13.98% | $12,938,129.20 |
| SEI/USDT:USDT | +10.50% | $19,270,375.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.51% | +3.44% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.62% | +2.55% |
| LUNC/USDT:USDT | below_1h_threshold | +2.19% | +2.12% |
| SEI/USDT:USDT | below_1h_threshold | +2.02% | +1.95% |
| HYPE/USDT:USDT | below_1h_threshold | +1.37% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
