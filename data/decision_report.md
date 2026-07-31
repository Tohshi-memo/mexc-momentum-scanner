# Decision Report

- generated_at: 2026-07-31T07:31:26.427472+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9972**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9972, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.44% | **+0.97%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.14% | **+0.92%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.27% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +7.36% | **+0.74%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.80% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.61% | **+1.52%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.32% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_BB3S_LONG | 10/10 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.80% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$561.30** / 初期 $100.00 (+461.30%)
- 確定: 3563件 (Win 1139 / Loss 1160 / Flat 1264) / skip 2970件
- 成長率目線: 平均log +0.000484 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $561.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.08** / 初期 $100.00 (+43.08%)
- 確定: 1266件 (Win 357 / Loss 290 / Flat 619) / skip 2117件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1715 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $143.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.75** / 初期 $100.00 (+10.75%)
- 確定: 809件 (Win 263 / Loss 321 / Flat 225) / pending 6件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000484 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $110.75

## 6. Latest Market Context

- 更新: 2026-07-31T07:31:17.504625+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=63951.4
- Funnel: target 920 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +61.41% | $10,387,217.73 |
| GIGGLE/USDT:USDT | +35.34% | $2,590,887.70 |
| MMT/USDT:USDT | +31.95% | $12,171,172.66 |
| AXTISTOCK/USDT:USDT | +31.37% | $4,555,840.55 |
| BULLA/USDT:USDT | +27.63% | $1,252,536.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +4.18% | +4.58% |
| US/USDT:USDT | below_1h_threshold | +2.72% | +3.12% |
| CAP/USDT:USDT | below_1h_threshold | +1.87% | +2.28% |
| SAND/USDT:USDT | below_1h_threshold | +1.60% | +2.00% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.51% | +1.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
