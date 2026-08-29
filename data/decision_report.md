# Decision Report

- generated_at: 2026-08-29T18:41:23.195336+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12958**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12958, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.27% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.68%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.50% | **+0.88%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.31% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$749.35** / 初期 $100.00 (+649.35%)
- 確定: 4728件 (Win 1436 / Loss 1551 / Flat 1741) / skip 4791件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $749.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$162.94** / 初期 $100.00 (+62.94%)
- 確定: 2042件 (Win 561 / Loss 489 / Flat 992) / skip 4327件
- 成長率目線: 平均log +0.000239 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0799 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $162.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2392件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000173 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-29T18:41:13.359147+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=78159.7
- Funnel: target 1023 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +19.16% | $7,360,127.31 |
| FONE/USDT:USDT | +17.42% | $1,172,104.72 |
| PONS/USDT:USDT | +9.46% | $1,011,337.70 |
| BTR/USDT:USDT | +6.13% | $9,588,263.60 |
| NIL/USDT:USDT | +5.43% | $6,845,674.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +3.43% | +3.32% |
| COTI/USDT:USDT | below_1h_threshold | +2.97% | +2.86% |
| MOVR/USDT:USDT | below_1h_threshold | +2.54% | +2.43% |
| PONS/USDT:USDT | below_1h_threshold | +1.46% | +1.35% |
| EDEN/USDT:USDT | below_1h_threshold | +1.43% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
