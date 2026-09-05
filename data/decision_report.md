# Decision Report

- generated_at: 2026-09-05T17:16:25.595833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13759**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13759, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.77% | **+0.31%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.19% | **-0.15%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.50% | **+1.13%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +1.82% | **+0.82%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.87% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.91** / 初期 $100.00 (+759.91%)
- 確定: 5065件 (Win 1521 / Loss 1652 / Flat 1892) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $859.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.52** / 初期 $100.00 (+88.52%)
- 確定: 2504件 (Win 698 / Loss 590 / Flat 1216) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0256 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.53** / 初期 $100.00 (+19.53%)
- 確定: 2380件 (Win 706 / Loss 903 / Flat 771) / pending 6件 / skip 2848件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.53

## 6. Latest Market Context

- 更新: 2026-09-05T17:16:13.129551+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80031.4
- Funnel: target 1050 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1, 4h RSI 73.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +18.06% | $2,239,387.26 |
| 4/USDT:USDT | +15.93% | $24,250,905.83 |
| USELESS/USDT:USDT | +11.70% | $20,114,442.60 |
| MAGMA/USDT:USDT | +11.31% | $2,128,618.47 |
| BASECAT/USDT:USDT | +6.28% | $1,998,030.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.89% | +4.85% |
| PONS/USDT:USDT | below_1h_threshold | +3.29% | +3.25% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.61% | +2.58% |
| AKE/USDT:USDT | below_1h_threshold | +2.32% | +2.28% |
| DOGE/USDT:USDT | below_1h_threshold | +1.34% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
