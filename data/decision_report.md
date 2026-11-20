# Decision Report

- generated_at: 2026-11-20T07:16:33.343077+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19232**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19232, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.52% | **+0.76%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.99% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.45% | **+0.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.24% | **+0.43%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.56% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,701.37** / 初期 $100.00 (+1601.37%)
- 確定: 7386件 (Win 2122 / Loss 2378 / Flat 2886) / skip 8407件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HUMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,701.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.95** / 初期 $100.00 (+339.95%)
- 確定: 5056件 (Win 1350 / Loss 1087 / Flat 2619) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0000 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $439.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7390件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000238 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T07:16:15.864039+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=61982.7
- Funnel: target 1084 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +31.92% | $10,232,454.54 |
| BARD/USDT:USDT | +20.04% | $2,145,689.17 |
| SOXS/USDT:USDT | +18.60% | $54,833,358.79 |
| ICNT/USDT:USDT | +15.93% | $5,949,109.18 |
| UVXY/USDT:USDT | +13.35% | $3,688,994.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +3.68% | +3.76% |
| BLESS/USDT:USDT | below_1h_threshold | +3.43% | +3.51% |
| BARD/USDT:USDT | below_1h_threshold | +1.19% | +1.27% |
| RAVE/USDT:USDT | below_1h_threshold | +0.94% | +1.02% |
| BTW/USDT:USDT | below_1h_threshold | +0.76% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
