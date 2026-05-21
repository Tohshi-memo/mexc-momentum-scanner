# Decision Report

- generated_at: 2026-05-21T07:48:53.737963+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4615**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=4615, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| ASK | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.35% | **+1.02%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.38% | **+0.97%** |
| LIMIT_BB3S | 6/20 | 30.0% | +2.98% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.68% | **+1.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.19% | **+0.09%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 631件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T07:48:51.670736+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=77728.1
- Funnel: target 765 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +41.36% | $1,984,768.37 |
| EDEN/USDT:USDT | +33.92% | $30,515,796.40 |
| USELESS/USDT:USDT | +19.75% | $1,589,769.91 |
| UAI/USDT:USDT | +14.35% | $1,030,988.73 |
| SATO/USDT:USDT | +13.87% | $3,591,066.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +3.18% | +3.00% |
| LIT/USDT:USDT | below_1h_threshold | +2.91% | +2.73% |
| HYPE/USDT:USDT | below_1h_threshold | +2.64% | +2.46% |
| SPX/USDT:USDT | below_1h_threshold | +2.17% | +1.99% |
| USELESS/USDT:USDT | below_1h_threshold | +1.90% | +1.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
