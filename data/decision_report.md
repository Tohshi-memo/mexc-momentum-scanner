# Decision Report

- generated_at: 2026-08-29T23:31:33.441334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12973**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12973, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.79% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.78% | **+2.50%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.21% | **+2.41%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.29% | **+2.30%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.50% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$753.45** / 初期 $100.00 (+653.45%)
- 確定: 4743件 (Win 1442 / Loss 1558 / Flat 1743) / skip 4791件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.07% 残高後 $753.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$167.60** / 初期 $100.00 (+67.60%)
- 確定: 2057件 (Win 569 / Loss 494 / Flat 994) / skip 4327件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1448 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.04% 残高後 $167.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2409件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000371 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-29T23:31:20.262077+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78234.8
- Funnel: target 1023 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +25.94% | $9,397,770.68 |
| HNT/USDT:USDT | +18.45% | $22,407,853.30 |
| BTR/USDT:USDT | +17.19% | $9,818,011.84 |
| FONE/USDT:USDT | +16.86% | $1,244,136.86 |
| BTW/USDT:USDT | +13.84% | $3,963,767.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKR/USDT:USDT | below_1h_threshold | +3.09% | +3.04% |
| VET/USDT:USDT | below_1h_threshold | +2.95% | +2.90% |
| PONS/USDT:USDT | below_1h_threshold | +2.39% | +2.34% |
| LIT/USDT:USDT | below_1h_threshold | +1.45% | +1.39% |
| BTR/USDT:USDT | below_1h_threshold | +1.24% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
