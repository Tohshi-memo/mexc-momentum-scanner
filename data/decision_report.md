# Decision Report

- generated_at: 2026-10-25T16:41:24.893104+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17432**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17432, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.06% | **+0.06%** |
| LIMIT_ATR | 6/20 | 30.0% | +0.17% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.03% | **+1.93%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.99% | **+1.75%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.05% | **+1.64%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,575.16** / 初期 $100.00 (+1475.16%)
- 確定: 6685件 (Win 1946 / Loss 2130 / Flat 2609) / skip 7308件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,575.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$319.30** / 初期 $100.00 (+219.30%)
- 確定: 3975件 (Win 1104 / Loss 934 / Flat 1937) / skip 6868件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1956 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $319.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5592件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000586 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T16:41:12.691501+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=80524.9
- Funnel: target 1070 → liquid 117 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +9.11% | $2,165,728.50 |
| BIRB/USDT:USDT | +1.97% | $1,820,477.83 |
| VVV/USDT:USDT | +1.37% | $1,623,947.63 |
| TAG/USDT:USDT | +1.04% | $2,181,977.79 |
| MAGMA/USDT:USDT | +0.75% | $1,135,571.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIRB/USDT:USDT | below_1h_threshold | +1.97% | +2.07% |
| VVV/USDT:USDT | below_1h_threshold | +1.37% | +1.47% |
| TAG/USDT:USDT | below_1h_threshold | +1.04% | +1.14% |
| ORDER/USDT:USDT | below_1h_threshold | +0.79% | +0.88% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.67% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
