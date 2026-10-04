# Decision Report

- generated_at: 2026-10-04T20:26:15.666687+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16127**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=16127, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +3.60% | **+1.62%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +2.25% | **+1.24%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.79% | **+0.99%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.85% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,312.14** / 初期 $100.00 (+1212.14%)
- 確定: 6186件 (Win 1821 / Loss 1984 / Flat 2381) / skip 6502件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $1,312.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3609件 (Win 1005 / Loss 845 / Flat 1759) / skip 5929件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0856 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4285件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000306 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-04T20:26:04.264604+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=85427.1
- Funnel: target 1076 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +103.71% | $6,551,346.16 |
| HNT/USDT:USDT | +8.12% | $1,941,296.37 |
| SKY/USDT:USDT | +5.38% | $1,917,262.92 |
| VVV/USDT:USDT | +5.30% | $1,995,713.21 |
| CHIP/USDT:USDT | +5.26% | $2,162,874.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HNT/USDT:USDT | below_1h_threshold | +4.11% | +4.06% |
| CHIP/USDT:USDT | below_1h_threshold | +1.76% | +1.71% |
| SKY/USDT:USDT | below_1h_threshold | +1.17% | +1.13% |
| BATON/USDT:USDT | below_1h_threshold | +1.10% | +1.05% |
| LSK/USDT:USDT | below_1h_threshold | +0.82% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
