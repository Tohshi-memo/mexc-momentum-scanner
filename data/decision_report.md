# Decision Report

- generated_at: 2026-11-09T09:01:22.795377+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18510**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18510, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.83% | **+0.99%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.11% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.90% | **+1.52%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7162件 (Win 2057 / Loss 2285 / Flat 2820) / skip 7909件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4757件 (Win 1277 / Loss 1047 / Flat 2433) / skip 7164件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0579 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6672件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-09T09:01:09.832648+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=74509.0
- Funnel: target 1089 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RITUAL/USDT:USDT | +49.16% | $1,295,701.94 |
| AIOT/USDT:USDT | +14.83% | $7,134,168.96 |
| PIEVERSE/USDT:USDT | +9.05% | $1,291,642.54 |
| ANSEM/USDT:USDT | +6.95% | $1,127,510.72 |
| DELTAELECSTOCK/USDT:USDT | +4.78% | $1,646,565.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.94% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +1.76% | +1.78% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.60% | +1.62% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +1.53% | +1.55% |
| RITUAL/USDT:USDT | below_1h_threshold | +1.08% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
