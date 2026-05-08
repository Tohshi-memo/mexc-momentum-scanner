# Decision Report

- generated_at: 2026-05-08T18:07:39.209196+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3814**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.52% / filled 20/20。**
- 全期間 MARKET基準: n=3814, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |
| ASK | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.75% | **+0.64%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.91% | **+0.51%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.42% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.68% | **+0.38%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.18% | **-0.10%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.17% | **-0.12%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.66% | **-0.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 183件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T18:07:36.415241+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=80150.4
- Funnel: target 768 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +7.86% | $49,816,116.59 |
| AKT/USDT:USDT | +7.66% | $1,078,869.85 |
| COLLECT/USDT:USDT | +7.41% | $1,621,821.69 |
| IO/USDT:USDT | +6.97% | $1,313,466.33 |
| INTCSTOCK/USDT:USDT | +6.57% | $8,300,290.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_1h_threshold | +3.80% | +3.64% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.72% | +1.56% |
| PYTH/USDT:USDT | below_1h_threshold | +1.44% | +1.28% |
| SIREN/USDT:USDT | below_1h_threshold | +1.44% | +1.28% |
| PLAY/USDT:USDT | below_1h_threshold | +1.35% | +1.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
