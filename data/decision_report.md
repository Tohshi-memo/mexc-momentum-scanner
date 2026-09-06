# Decision Report

- generated_at: 2026-09-06T00:21:26.778613+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13784**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13784, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.67% | **+0.23%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 2/13 | 15.4% | -1.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.09% | **+1.19%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.34% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.18% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$867.36** / 初期 $100.00 (+767.36%)
- 確定: 5090件 (Win 1527 / Loss 1659 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.72% 残高後 $867.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.23** / 初期 $100.00 (+89.23%)
- 確定: 2529件 (Win 705 / Loss 598 / Flat 1226) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0421 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $189.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.12** / 初期 $100.00 (+20.12%)
- 確定: 2401件 (Win 714 / Loss 910 / Flat 777) / pending 4件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000283 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARB/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $120.12

## 6. Latest Market Context

- 更新: 2026-09-06T00:21:13.268851+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79878.8
- Funnel: target 1050 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +40.00% | $81,067,344.51 |
| BASECAT/USDT:USDT | +21.40% | $1,962,256.88 |
| SUSHI/USDT:USDT | +17.98% | $3,801,823.33 |
| 4/USDT:USDT | +17.51% | $21,574,139.68 |
| MAGMA/USDT:USDT | +17.27% | $2,465,547.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARB/USDT:USDT | below_1h_threshold | +4.93% | +4.83% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.54% | +2.44% |
| TUT/USDT:USDT | below_1h_threshold | +2.53% | +2.43% |
| ENA/USDT:USDT | below_1h_threshold | +2.02% | +1.92% |
| INJ/USDT:USDT | below_1h_threshold | +1.74% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
