# Decision Report

- generated_at: 2026-10-24T02:06:23.175059+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17324**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17324, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +1.35% | **+0.54%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_10PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.50% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +1.90% | **+0.85%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +1.51% | **+0.75%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.43** / 初期 $100.00 (+1210.43%)
- 確定: 6578件 (Win 1905 / Loss 2100 / Flat 2573) / skip 7307件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,310.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6806件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0991 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5483件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000314 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T02:06:08.374460+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80891.9
- Funnel: target 1088 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +71.14% | $6,383,008.54 |
| IRYS/USDT:USDT | +53.53% | $99,429,261.17 |
| AXIS/USDT:USDT | +24.33% | $2,089,393.79 |
| AGT/USDT:USDT | +16.13% | $10,805,597.97 |
| SOXS/USDT:USDT | +3.28% | $29,295,830.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.48% | +0.49% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.40% | +0.41% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.38% | +0.39% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.35% | +0.35% |
| BTW/USDT:USDT | below_1h_threshold | +0.34% | +0.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
