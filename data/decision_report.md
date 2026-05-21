# Decision Report

- generated_at: 2026-05-21T12:23:54.612271+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4623**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=4623, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.43% | **+1.36%** |
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_BB3S | 6/18 | 33.3% | +3.04% | **+1.01%** |
| ASK | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.23% | **+0.13%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.07% | **+0.03%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.13% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 638件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T12:23:50.209842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77087.9
- Funnel: target 766 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROVE/USDT:USDT | +41.36% | $5,642,445.54 |
| EDEN/USDT:USDT | +40.94% | $30,913,712.88 |
| ROAM/USDT:USDT | +30.64% | $2,259,062.03 |
| PEAQ/USDT:USDT | +27.30% | $1,151,888.50 |
| MITO/USDT:USDT | +25.85% | $1,275,456.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.17% | +4.26% |
| EDEN/USDT:USDT | below_1h_threshold | +4.07% | +4.16% |
| USELESS/USDT:USDT | below_1h_threshold | +1.79% | +1.88% |
| UAI/USDT:USDT | below_1h_threshold | +0.80% | +0.89% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.60% | +0.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
