# Decision Report

- generated_at: 2026-08-04T01:01:19.741877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10259**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=10259, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.58% | **+0.06%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.23% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$584.04** / 初期 $100.00 (+484.04%)
- 確定: 3717件 (Win 1177 / Loss 1217 / Flat 1323) / skip 3103件
- 成長率目線: 平均log +0.000475 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $584.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1284件 (Win 359 / Loss 299 / Flat 626) / skip 2386件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0352 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.45** / 初期 $100.00 (+16.45%)
- 確定: 1032件 (Win 332 / Loss 400 / Flat 300) / pending 3件 / skip 694件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000402 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.45

## 6. Latest Market Context

- 更新: 2026-08-04T01:01:13.971475+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=63364.5
- Funnel: target 929 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLTRSTOCK/USDT:USDT | +14.31% | $3,551,805.14 |
| KOMA/USDT:USDT | +11.92% | $2,151,496.78 |
| PIPPIN/USDT:USDT | +10.91% | $7,542,212.50 |
| ON/USDT:USDT | +10.82% | $2,767,489.59 |
| UAI/USDT:USDT | +10.58% | $12,145,291.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USOIL/USDT:USDT | below_1h_threshold | +0.95% | +0.89% |
| VANRY/USDT:USDT | below_1h_threshold | +0.37% | +0.32% |
| BANK/USDT:USDT | below_1h_threshold | +0.36% | +0.30% |
| FHE/USDT:USDT | below_1h_threshold | +0.34% | +0.29% |
| APE/USDT:USDT | below_1h_threshold | +0.30% | +0.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
