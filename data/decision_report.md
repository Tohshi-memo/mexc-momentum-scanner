# Decision Report

- generated_at: 2026-07-14T08:11:15.404125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8679**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8679, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.73% | **+0.26%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.54% | **+2.54%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.90% | **+1.72%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.23% | **+0.89%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.71** / 初期 $100.00 (+230.71%)
- 確定: 2847件 (Win 891 / Loss 924 / Flat 1032) / skip 2393件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $330.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.98** / 初期 $100.00 (+4.98%)
- 確定: 677件 (Win 159 / Loss 161 / Flat 357) / skip 1413件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0520 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $104.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 59件 (Win 19 / Loss 39 / Flat 1) / pending 0件 / skip 90件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000118 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SXT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-14T08:11:10.464460+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=62492.0
- Funnel: target 862 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +36.97% | $7,945,841.33 |
| TRIA/USDT:USDT | +29.00% | $3,368,628.41 |
| SXT/USDT:USDT | +22.17% | $2,991,540.25 |
| BSB/USDT:USDT | +17.35% | $2,606,809.04 |
| ZBT/USDT:USDT | +17.18% | $3,420,440.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SXT/USDT:USDT | below_1h_threshold | +2.95% | +3.01% |
| ENA/USDT:USDT | below_1h_threshold | +1.43% | +1.49% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.41% | +1.47% |
| AIOT/USDT:USDT | below_1h_threshold | +1.30% | +1.36% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.04% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
