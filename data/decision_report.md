# Decision Report

- generated_at: 2026-10-25T07:01:18.490860+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17410**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17410, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +1.79% | **+1.61%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.12% | **+0.90%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.18% | **+0.65%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.18% | **+1.75%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.10% | **+1.57%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.27% | **+1.47%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.78% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,501.14** / 初期 $100.00 (+1401.14%)
- 確定: 6663件 (Win 1936 / Loss 2123 / Flat 2604) / skip 7308件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,501.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$309.10** / 初期 $100.00 (+209.10%)
- 確定: 3953件 (Win 1094 / Loss 927 / Flat 1932) / skip 6868件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1793 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $309.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5568件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000563 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T07:01:06.115776+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80498.0
- Funnel: target 1071 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +43.71% | $3,393,753.76 |
| APR/USDT:USDT | +42.84% | $5,380,120.11 |
| USELESS/USDT:USDT | +20.23% | $4,144,420.13 |
| AGT/USDT:USDT | +15.37% | $5,474,487.45 |
| GRASS/USDT:USDT | +10.27% | $1,841,286.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +0.48% | +0.43% |
| NIL/USDT:USDT | below_1h_threshold | +0.37% | +0.32% |
| APR/USDT:USDT | below_1h_threshold | +0.22% | +0.17% |
| GRAM/USDT:USDT | below_1h_threshold | +0.16% | +0.11% |
| CHIP/USDT:USDT | below_1h_threshold | +0.16% | +0.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
