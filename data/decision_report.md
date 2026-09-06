# Decision Report

- generated_at: 2026-09-06T14:36:17.680411+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13820**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.82% / filled 20/20。**
- 全期間 MARKET基準: n=13820, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.82% | **+2.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.82% | **+2.82%** |
| LIMIT_1PCT | 15/20 | 75.0% | +2.52% | **+1.89%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.29% | **+1.26%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.40% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.74% | **-0.15%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | -0.54% | **-0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$841.39** / 初期 $100.00 (+741.39%)
- 確定: 5126件 (Win 1538 / Loss 1679 / Flat 1909) / skip 5255件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JUP/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $841.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.84** / 初期 $100.00 (+90.84%)
- 確定: 2564件 (Win 717 / Loss 614 / Flat 1233) / skip 4667件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0510 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JUP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $190.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.47** / 初期 $100.00 (+19.47%)
- 確定: 2431件 (Win 724 / Loss 927 / Flat 780) / pending 1件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JUP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.47

## 6. Latest Market Context

- 更新: 2026-09-06T14:36:08.451935+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=79549.9
- Funnel: target 1054 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAY/USDT:USDT | +56.80% | $8,711,873.68 |
| ARB/USDT:USDT | +41.38% | $184,511,810.03 |
| FLOCK/USDT:USDT | +31.80% | $2,516,671.82 |
| FONE/USDT:USDT | +28.58% | $1,110,923.73 |
| COTI/USDT:USDT | +25.23% | $1,752,421.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +4.11% | +4.41% |
| FLOCK/USDT:USDT | below_1h_threshold | +2.28% | +2.58% |
| UAI/USDT:USDT | below_1h_threshold | +1.18% | +1.48% |
| BLESS/USDT:USDT | below_1h_threshold | +0.79% | +1.10% |
| XAN/USDT:USDT | below_1h_threshold | +0.64% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
