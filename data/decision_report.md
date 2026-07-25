# Decision Report

- generated_at: 2026-07-25T07:56:24.811966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9497**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9497, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.59% | **+0.48%** |
| LIMIT_6PCT | 2/20 | 10.0% | +3.33% | **+0.33%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.69% | **-0.24%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.38% | **-0.32%** |
| LIMIT_ATR | 15/20 | 75.0% | -1.09% | **-0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.66% | **+2.26%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.42% | **+2.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.80% | **+1.12%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.24% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.58** / 初期 $100.00 (+326.58%)
- 確定: 3329件 (Win 1050 / Loss 1078 / Flat 1201) / skip 2729件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $426.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1743件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1425 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$105.51** / 初期 $100.00 (+5.51%)
- 確定: 545件 (Win 182 / Loss 210 / Flat 153) / pending 6件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000439 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $105.51

## 6. Latest Market Context

- 更新: 2026-07-25T07:56:13.315274+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63986.7
- Funnel: target 898 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +110.89% | $74,106,734.75 |
| EUL/USDT:USDT | +43.27% | $2,823,826.50 |
| AKE/USDT:USDT | +27.48% | $47,182,211.33 |
| B2/USDT:USDT | +18.07% | $3,208,048.78 |
| ZAMA/USDT:USDT | +13.62% | $5,007,677.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAITO/USDT:USDT | below_1h_threshold | +2.68% | +2.68% |
| UB/USDT:USDT | below_1h_threshold | +2.00% | +1.99% |
| RIF/USDT:USDT | below_1h_threshold | +1.81% | +1.81% |
| XMR/USDT:USDT | below_1h_threshold | +1.36% | +1.36% |
| VVV/USDT:USDT | below_1h_threshold | +1.21% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
