# Decision Report

- generated_at: 2026-05-27T19:15:23.028139+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4939**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.74% / filled 20/20。**
- 全期間 MARKET基準: n=4939, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.74% | **+0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +3.37% | **+2.36%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.67% | **+2.27%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.79% | **+1.61%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.80% | **+1.40%** |
| MARKET | 20/20 | 100.0% | +0.74% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +2.67% | **+1.60%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.89% | **+1.23%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$96.19** / 初期 $100.00 (-3.81%)
- 確定トレード: 67件 (TP 18 / SL 46 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 816件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T19:15:20.885198+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=75009.5
- Funnel: target 771 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HIGH/USDT:USDT | +6.13% | $1,009,417.71 |
| XLM/USDT:USDT | +4.73% | $32,224,579.29 |
| NEAR/USDT:USDT | +4.26% | $165,560,343.66 |
| GENIUS/USDT:USDT | +4.10% | $1,223,623.42 |
| JTO/USDT:USDT | +3.71% | $1,616,476.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +3.95% | +3.93% |
| NEAR/USDT:USDT | below_1h_threshold | +2.79% | +2.78% |
| XLM/USDT:USDT | below_1h_threshold | +2.25% | +2.24% |
| NIL/USDT:USDT | below_1h_threshold | +1.23% | +1.22% |
| FET/USDT:USDT | below_1h_threshold | +1.12% | +1.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
