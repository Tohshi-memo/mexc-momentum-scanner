# Decision Report

- generated_at: 2026-07-25T08:11:18.339092+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9498**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9498, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +1.72% | **+0.43%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.14% | **-0.12%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -1.28% | **-0.39%** |
| LIMIT_ATR | 15/20 | 75.0% | -1.10% | **-0.82%** |
| LIMIT_3PCT | 17/20 | 85.0% | -1.05% | **-0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.28% | **+2.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.48% | **+2.11%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.38% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.24% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$429.27** / 初期 $100.00 (+329.27%)
- 確定: 3330件 (Win 1051 / Loss 1078 / Flat 1201) / skip 2729件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $429.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1744件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1449 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$105.79** / 初期 $100.00 (+5.79%)
- 確定: 546件 (Win 183 / Loss 210 / Flat 153) / pending 5件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000431 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $105.79

## 6. Latest Market Context

- 更新: 2026-07-25T08:11:11.517053+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63906.6
- Funnel: target 897 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +111.53% | $76,482,965.92 |
| EUL/USDT:USDT | +41.61% | $3,094,227.22 |
| AKE/USDT:USDT | +27.49% | $46,809,202.42 |
| B2/USDT:USDT | +17.92% | $3,140,701.65 |
| ZAMA/USDT:USDT | +12.95% | $5,243,043.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +1.02% | +1.12% |
| KAS/USDT:USDT | below_1h_threshold | +1.02% | +1.12% |
| BASED/USDT:USDT | below_1h_threshold | +0.78% | +0.89% |
| B2/USDT:USDT | below_1h_threshold | +0.73% | +0.84% |
| RIF/USDT:USDT | below_1h_threshold | +0.66% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
