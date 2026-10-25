# Decision Report

- generated_at: 2026-10-25T01:16:19.127335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17390**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17390, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.81% | **-0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.71% | **+1.08%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.33% | **+0.73%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.08% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.91% | **+1.62%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.54% | **+1.01%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,443.78** / 初期 $100.00 (+1343.78%)
- 確定: 6643件 (Win 1927 / Loss 2117 / Flat 2599) / skip 7308件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,443.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$301.11** / 初期 $100.00 (+201.11%)
- 確定: 3933件 (Win 1085 / Loss 921 / Flat 1927) / skip 6868件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2348 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ORDER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $301.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5549件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000721 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T01:16:09.109513+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=80755.1
- Funnel: target 1079 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +44.81% | $1,095,193.65 |
| LIGHT/USDT:USDT | +19.70% | $1,148,409.54 |
| USELESS/USDT:USDT | +15.52% | $2,966,286.87 |
| AGT/USDT:USDT | +14.76% | $6,026,862.51 |
| GRASS/USDT:USDT | +9.01% | $1,696,776.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +0.47% | +0.58% |
| MUU/USDT:USDT | below_1h_threshold | +0.41% | +0.52% |
| USELESS/USDT:USDT | below_1h_threshold | +0.38% | +0.49% |
| SNXX/USDT:USDT | below_1h_threshold | +0.37% | +0.48% |
| VVV/USDT:USDT | below_1h_threshold | +0.25% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
