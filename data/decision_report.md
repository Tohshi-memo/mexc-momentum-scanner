# Decision Report

- generated_at: 2026-08-24T23:56:23.148723+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12552**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12552, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.14% | **-0.03%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.35% | **-0.10%** |
| LIMIT_8PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +3.52% | **+2.46%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.16% | **+2.21%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.69% | **+1.61%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.51% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$691.25** / 初期 $100.00 (+591.25%)
- 確定: 4533件 (Win 1382 / Loss 1488 / Flat 1663) / skip 4580件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $691.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3990件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0605 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1913件 (Win 561 / Loss 728 / Flat 624) / pending 0件 / skip 2114件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-24T23:56:14.041986+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78800.7
- Funnel: target 1022 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +83.08% | $3,456,160.31 |
| STORJ/USDT:USDT | +20.81% | $4,760,094.57 |
| CASHCAT/USDT:USDT | +12.82% | $2,589,843.78 |
| ONG/USDT:USDT | +11.39% | $2,397,693.51 |
| US/USDT:USDT | +7.21% | $1,966,308.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +4.34% | +4.22% |
| BEAT/USDT:USDT | below_1h_threshold | +2.65% | +2.52% |
| PONS/USDT:USDT | below_1h_threshold | +1.96% | +1.84% |
| CRV/USDT:USDT | below_1h_threshold | +1.74% | +1.62% |
| HYPE/USDT:USDT | below_1h_threshold | +1.42% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
