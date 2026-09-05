# Decision Report

- generated_at: 2026-09-05T16:51:32.942287+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13753**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13753, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.38% | **-1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.42% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.50% | **+1.37%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.14% | **+0.96%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$856.50** / 初期 $100.00 (+756.50%)
- 確定: 5059件 (Win 1520 / Loss 1651 / Flat 1888) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $856.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.37** / 初期 $100.00 (+88.37%)
- 確定: 2498件 (Win 697 / Loss 589 / Flat 1212) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0458 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.43** / 初期 $100.00 (+19.43%)
- 確定: 2377件 (Win 705 / Loss 902 / Flat 770) / pending 6件 / skip 2845件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000262 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.43

## 6. Latest Market Context

- 更新: 2026-09-05T16:51:20.040018+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=79958.5
- Funnel: target 1050 → liquid 132 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1, 4h RSI 76.7 >= 65=1, 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +15.82% | $24,071,767.92 |
| USELESS/USDT:USDT | +10.42% | $20,997,821.98 |
| BASECAT/USDT:USDT | +5.99% | $1,997,238.63 |
| MAGMA/USDT:USDT | +5.92% | $2,232,201.21 |
| UNI/USDT:USDT | +4.87% | $29,641,294.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_relative_strength | +5.03% | +4.78% |
| NIULAI/USDT:USDT | below_1h_threshold | +4.67% | +4.42% |
| HNT/USDT:USDT | below_1h_threshold | +4.16% | +3.91% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.09% | +2.84% |
| EDGE/USDT:USDT | below_1h_threshold | +2.88% | +2.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
