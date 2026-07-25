# Decision Report

- generated_at: 2026-07-25T16:16:21.821232+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9528**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9528, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.09% | **-1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/17 | 29.4% | +2.64% | **+0.78%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.05% | **+2.44%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.30% | **+1.95%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.22% | **+1.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$444.60** / 初期 $100.00 (+344.60%)
- 確定: 3356件 (Win 1062 / Loss 1087 / Flat 1207) / skip 2733件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $444.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$135.33** / 初期 $100.00 (+35.33%)
- 確定: 1181件 (Win 322 / Loss 257 / Flat 602) / skip 1758件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1708 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $135.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.96** / 初期 $100.00 (+7.96%)
- 確定: 575件 (Win 195 / Loss 220 / Flat 160) / pending 6件 / skip 421件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000538 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $107.96

## 6. Latest Market Context

- 更新: 2026-07-25T16:16:12.889899+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64168.0
- Funnel: target 898 → liquid 138 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +9.80% | $133,053,307.63 |
| BANK/USDT:USDT | +9.17% | $85,615,984.37 |
| ALLO/USDT:USDT | +4.86% | $14,654,917.61 |
| SHIB/USDT:USDT | +3.28% | $7,936,040.85 |
| RIF/USDT:USDT | +2.64% | $3,716,220.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.60% | +4.57% |
| SHIB/USDT:USDT | below_1h_threshold | +3.43% | +3.40% |
| RIF/USDT:USDT | below_1h_threshold | +2.64% | +2.61% |
| BASED/USDT:USDT | below_1h_threshold | +2.60% | +2.57% |
| FLOKI/USDT:USDT | below_1h_threshold | +2.40% | +2.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
