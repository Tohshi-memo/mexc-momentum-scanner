# Decision Report

- generated_at: 2026-07-25T21:46:21.928468+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9541**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9541, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.30% | **+0.09%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 11/20 | 55.0% | -0.16% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.95% | **+1.66%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.90% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.56% | **+0.22%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.47% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$458.27** / 初期 $100.00 (+358.27%)
- 確定: 3369件 (Win 1070 / Loss 1091 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000452 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $458.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$138.09** / 初期 $100.00 (+38.09%)
- 確定: 1194件 (Win 330 / Loss 261 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1712 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $138.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.05** / 初期 $100.00 (+8.05%)
- 確定: 585件 (Win 198 / Loss 224 / Flat 163) / pending 5件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000524 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.05

## 6. Latest Market Context

- 更新: 2026-07-25T21:46:14.737805+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64309.5
- Funnel: target 898 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +17.76% | $18,333,780.83 |
| ESPORTS/USDT:USDT | +17.50% | $25,761,250.25 |
| ALLO/USDT:USDT | +12.53% | $17,952,154.23 |
| DEXE/USDT:USDT | +12.29% | $125,829,268.01 |
| VELVET/USDT:USDT | +11.11% | $8,096,099.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.70% | +1.69% |
| FET/USDT:USDT | below_1h_threshold | +1.41% | +1.40% |
| KAITO/USDT:USDT | below_1h_threshold | +1.15% | +1.14% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.04% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
