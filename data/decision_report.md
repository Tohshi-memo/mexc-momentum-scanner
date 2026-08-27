# Decision Report

- generated_at: 2026-08-27T19:01:26.546588+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12832**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=12832, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.47% | **+1.98%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.14% | **+1.82%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.98% | **+0.58%** |
| LIMIT_5PCT | 2/20 | 10.0% | +1.08% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +5.21% | **+0.52%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.03** / 初期 $100.00 (+616.03%)
- 確定: 4669件 (Win 1414 / Loss 1532 / Flat 1723) / skip 4724件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4240件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.79** / 初期 $100.00 (+14.79%)
- 確定: 1988件 (Win 580 / Loss 762 / Flat 646) / pending 0件 / skip 2317件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WIF/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.79

## 6. Latest Market Context

- 更新: 2026-08-27T19:01:17.168302+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80135.6
- Funnel: target 1019 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +11.39% | $21,144,586.76 |
| HEMI/USDT:USDT | +10.21% | $1,471,988.92 |
| UAI/USDT:USDT | +8.17% | $1,632,370.17 |
| VET/USDT:USDT | +4.04% | $7,556,488.94 |
| JUP/USDT:USDT | +4.00% | $2,522,640.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +1.93% | +1.91% |
| BMT/USDT:USDT | below_1h_threshold | +0.86% | +0.84% |
| SOXS/USDT:USDT | below_1h_threshold | +0.60% | +0.58% |
| JUP/USDT:USDT | below_1h_threshold | +0.60% | +0.58% |
| AKE/USDT:USDT | below_1h_threshold | +0.58% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
