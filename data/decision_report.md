# Decision Report

- generated_at: 2026-07-24T13:26:12.922769+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9441**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9441, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.55% | **+0.23%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.17% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.43% | **+1.07%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.52% | **+0.84%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3324件 (Win 1048 / Loss 1076 / Flat 1200) / skip 2678件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1164件 (Win 312 / Loss 254 / Flat 598) / skip 1688件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1181 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定: 501件 (Win 167 / Loss 196 / Flat 138) / pending 3件 / skip 407件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000362 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B2/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $103.40

## 6. Latest Market Context

- 更新: 2026-07-24T13:26:06.231334+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.64% price=64335.0
- Funnel: target 898 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +44.95% | $1,089,274.80 |
| ESPORTS/USDT:USDT | +40.72% | $12,982,039.29 |
| AKE/USDT:USDT | +26.73% | $38,205,926.11 |
| LA/USDT:USDT | +22.55% | $1,927,374.47 |
| RE/USDT:USDT | +22.28% | $21,827,651.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +2.54% | +3.17% |
| NGAS/USDT:USDT | below_1h_threshold | +1.64% | +2.28% |
| LA/USDT:USDT | below_1h_threshold | +1.45% | +2.08% |
| SOXS/USDT:USDT | below_1h_threshold | +1.31% | +1.95% |
| CAP/USDT:USDT | below_1h_threshold | +1.12% | +1.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
