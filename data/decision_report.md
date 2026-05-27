# Decision Report

- generated_at: 2026-05-27T13:02:11.519478+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4926**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.01% / filled 20/20。**
- 全期間 MARKET基準: n=4926, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.10% | **+1.10%** |
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.76%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.21% | **+0.19%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.10% | **+0.07%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.07% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 803件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T13:02:09.338990+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=75649.4
- Funnel: target 775 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +18.51% | $20,653,229.03 |
| RIF/USDT:USDT | +15.88% | $1,405,581.51 |
| LUNC/USDT:USDT | +13.73% | $15,246,951.05 |
| ALT/USDT:USDT | +13.33% | $2,742,296.43 |
| REQ/USDT:USDT | +12.91% | $1,696,130.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.82% | +0.83% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.72% | +0.73% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.57% | +0.58% |
| FILECOIN/USDT:USDT | below_1h_threshold | +0.47% | +0.47% |
| RIF/USDT:USDT | below_1h_threshold | +0.40% | +0.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
