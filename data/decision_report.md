# Decision Report

- generated_at: 2026-07-14T17:21:12.630711+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8699**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8699, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.66% | **-0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.62% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/10 | 90.0% | +2.56% | **+2.30%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.48% | **+1.98%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.97% | **+1.67%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.02% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$331.42** / 初期 $100.00 (+231.42%)
- 確定: 2862件 (Win 894 / Loss 930 / Flat 1038) / skip 2398件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.05% 残高後 $331.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.49** / 初期 $100.00 (+5.49%)
- 確定: 693件 (Win 161 / Loss 162 / Flat 370) / skip 1417件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0157 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 59件 (Win 19 / Loss 39 / Flat 1) / pending 0件 / skip 110件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000203 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SXT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-14T17:21:06.244929+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=64413.9
- Funnel: target 862 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +5.87% | $10,819,143.60 |
| US/USDT:USDT | +5.63% | $1,396,299.37 |
| SLX/USDT:USDT | +4.99% | $2,076,010.54 |
| SXT/USDT:USDT | +4.37% | $8,949,780.89 |
| RIVER/USDT:USDT | +3.66% | $1,671,746.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +2.52% | +2.97% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.32% | +2.77% |
| US/USDT:USDT | below_1h_threshold | +2.04% | +2.49% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +2.24% |
| VELVET/USDT:USDT | below_1h_threshold | +1.44% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
