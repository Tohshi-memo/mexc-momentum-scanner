# Decision Report

- generated_at: 2026-10-17T12:21:21.030975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16876**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.81% / filled 20/20。**
- 全期間 MARKET基準: n=16876, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.81% | **+1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.26% | **+1.07%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.72% | **+0.77%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.16% | **+0.75%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.11% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.99% | **+0.59%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,265.35** / 初期 $100.00 (+1165.35%)
- 確定: 6350件 (Win 1855 / Loss 2033 / Flat 2462) / skip 7087件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,265.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3690件 (Win 1027 / Loss 878 / Flat 1785) / skip 6597件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0439 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5035件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T12:21:09.552689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=81504.4
- Funnel: target 1084 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +86.21% | $19,647,980.23 |
| EPIC/USDT:USDT | +33.36% | $1,394,304.99 |
| Q/USDT:USDT | +31.81% | $1,011,884.97 |
| TMX/USDT:USDT | +16.66% | $1,195,043.06 |
| BTW/USDT:USDT | +14.94% | $23,518,488.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TMX/USDT:USDT | below_1h_threshold | +3.76% | +3.80% |
| Q/USDT:USDT | below_1h_threshold | +3.38% | +3.42% |
| BTW/USDT:USDT | below_1h_threshold | +2.77% | +2.82% |
| MAGIC/USDT:USDT | below_1h_threshold | +1.31% | +1.35% |
| EPIC/USDT:USDT | below_1h_threshold | +1.26% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
