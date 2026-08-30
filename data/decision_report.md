# Decision Report

- generated_at: 2026-08-30T04:56:23.036888+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13018**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13018, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.35% | **-2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +1.06% | **+0.91%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.09% | **+0.63%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.71% | **+0.60%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +5.00% | **+2.75%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +5.79% | **+2.60%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.57% | **+1.96%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.18% | **+1.59%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.09** / 初期 $100.00 (+692.09%)
- 確定: 4788件 (Win 1460 / Loss 1575 / Flat 1753) / skip 4791件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $792.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.90** / 初期 $100.00 (+73.90%)
- 確定: 2102件 (Win 589 / Loss 513 / Flat 1000) / skip 4327件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0645 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $173.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.33** / 初期 $100.00 (+17.33%)
- 確定: 2062件 (Win 607 / Loss 800 / Flat 655) / pending 4件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000398 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.33

## 6. Latest Market Context

- 更新: 2026-08-30T04:56:11.528799+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78044.7
- Funnel: target 1023 → liquid 119 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 89.8 >= 65=1, 4h RSI 88.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +67.86% | $29,719,179.58 |
| FONE/USDT:USDT | +65.65% | $1,374,706.08 |
| NIULAI/USDT:USDT | +62.23% | $2,459,467.23 |
| PONS/USDT:USDT | +42.37% | $1,520,820.18 |
| PROM/USDT:USDT | +31.04% | $14,512,121.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.62% | +4.69% |
| MOVR/USDT:USDT | below_1h_threshold | +3.76% | +3.84% |
| BTR/USDT:USDT | below_1h_threshold | +2.18% | +2.25% |
| BICO/USDT:USDT | below_1h_threshold | +2.15% | +2.22% |
| VET/USDT:USDT | below_1h_threshold | +2.10% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
