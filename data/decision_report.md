# Decision Report

- generated_at: 2026-10-03T08:06:21.089408+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16044**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=16044, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.21% | **+1.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.34% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.86% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.26** / 初期 $100.00 (+1191.26%)
- 確定: 6146件 (Win 1812 / Loss 1972 / Flat 2362) / skip 6459件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.46% 残高後 $1,291.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3606件 (Win 1005 / Loss 845 / Flat 1756) / skip 5849件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0320 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4205件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000162 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T08:06:10.159195+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=84559.8
- Funnel: target 1086 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +34.45% | $16,632,837.79 |
| SAND/USDT:USDT | +23.18% | $113,354,164.83 |
| VELVET/USDT:USDT | +13.60% | $10,767,304.03 |
| NIGHT/USDT:USDT | +13.02% | $12,811,122.53 |
| ONE/USDT:USDT | +8.48% | $1,434,113.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.84% | +2.78% |
| VELVET/USDT:USDT | below_1h_threshold | +2.27% | +2.21% |
| QNT/USDT:USDT | below_1h_threshold | +1.08% | +1.03% |
| CT/USDT:USDT | below_1h_threshold | +0.87% | +0.82% |
| NIL/USDT:USDT | below_1h_threshold | +0.79% | +0.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
