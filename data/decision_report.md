# Decision Report

- generated_at: 2026-07-19T14:26:19.463989+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9045**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9045, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.14% | **+1.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.88% | **+2.94%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.36% | **+1.06%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.49% | **+0.75%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.35** / 初期 $100.00 (+299.35%)
- 確定: 3107件 (Win 974 / Loss 991 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $399.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.52** / 初期 $100.00 (+26.52%)
- 確定: 1006件 (Win 259 / Loss 211 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0829 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $126.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.68** / 初期 $100.00 (+0.68%)
- 確定: 246件 (Win 83 / Loss 123 / Flat 40) / pending 5件 / skip 266件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.68

## 6. Latest Market Context

- 更新: 2026-07-19T14:26:11.754193+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64413.3
- Funnel: target 885 → liquid 126 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1, 4h RSI 90.6 >= 65=1, 4h RSI 77.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +154.88% | $43,377,586.91 |
| TLM/USDT:USDT | +78.24% | $8,758,544.68 |
| B/USDT:USDT | +51.73% | $32,449,563.58 |
| TAG/USDT:USDT | +25.07% | $4,818,137.69 |
| PI/USDT:USDT | +20.68% | $4,174,280.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +4.82% | +4.88% |
| AKE/USDT:USDT | below_1h_threshold | +4.69% | +4.75% |
| TLM/USDT:USDT | below_1h_threshold | +4.06% | +4.12% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.10% | +2.16% |
| ALLO/USDT:USDT | below_1h_threshold | +2.01% | +2.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
