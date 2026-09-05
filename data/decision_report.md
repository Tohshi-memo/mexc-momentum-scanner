# Decision Report

- generated_at: 2026-09-05T14:46:27.440874+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13740**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13740, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.37% | **+1.66%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.26% | **+1.47%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.40** / 初期 $100.00 (+757.40%)
- 確定: 5046件 (Win 1519 / Loss 1649 / Flat 1878) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $857.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.70** / 初期 $100.00 (+89.70%)
- 確定: 2485件 (Win 697 / Loss 587 / Flat 1201) / skip 4666件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0884 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $189.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.33** / 初期 $100.00 (+19.33%)
- 確定: 2365件 (Win 704 / Loss 901 / Flat 760) / pending 5件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $119.33

## 6. Latest Market Context

- 更新: 2026-09-05T14:46:14.978710+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=79684.9
- Funnel: target 1050 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +112.43% | $16,422,992.24 |
| 4/USDT:USDT | +64.00% | $21,920,711.31 |
| ICX/USDT:USDT | +44.01% | $1,132,730.93 |
| AKE/USDT:USDT | +40.22% | $19,981,750.04 |
| BASECAT/USDT:USDT | +38.58% | $1,887,695.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_relative_strength | +5.01% | +4.87% |
| BASECAT/USDT:USDT | below_1h_threshold | +3.82% | +3.68% |
| PONS/USDT:USDT | below_1h_threshold | +2.52% | +2.38% |
| CHIP/USDT:USDT | below_1h_threshold | +2.29% | +2.15% |
| AR/USDT:USDT | below_1h_threshold | +1.99% | +1.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
