# Decision Report

- generated_at: 2026-11-05T22:31:28.191519+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18209**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.85% / filled 20/20。**
- 全期間 MARKET基準: n=18209, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.90% | **+0.76%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.89% | **+0.35%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.05% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.27% | **+3.27%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.59% | **+0.33%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,507.12** / 初期 $100.00 (+1407.12%)
- 確定: 7017件 (Win 2022 / Loss 2243 / Flat 2752) / skip 7753件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SQQQ/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,507.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$374.94** / 初期 $100.00 (+274.94%)
- 確定: 4601件 (Win 1234 / Loss 1030 / Flat 2337) / skip 7019件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0575 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SQQQ/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $374.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6374件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000408 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T22:31:15.288439+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=75991.3
- Funnel: target 1084 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +14.20% | $5,153,702.57 |
| CLANKER/USDT:USDT | +13.20% | $9,244,642.73 |
| UVXY/USDT:USDT | +12.89% | $2,347,682.47 |
| BTW/USDT:USDT | +10.73% | $5,779,791.29 |
| IRENSTOCK/USDT:USDT | +8.84% | $2,707,063.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRENSTOCK/USDT:USDT | below_1h_threshold | +4.43% | +4.22% |
| UVXY/USDT:USDT | below_1h_threshold | +3.19% | +2.97% |
| ZEC/USDT:USDT | below_1h_threshold | +1.61% | +1.39% |
| CLANKER/USDT:USDT | below_1h_threshold | +1.56% | +1.35% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.49% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
