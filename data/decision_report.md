# Decision Report

- generated_at: 2026-07-19T11:06:16.304334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9024**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9024, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.17% | **-2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/19 | 26.3% | +2.42% | **+0.64%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.37% | **+2.37%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.67% | **+1.74%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.63% | **+0.92%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +1.30% | **+0.52%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +0.95% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.31** / 初期 $100.00 (+298.31%)
- 確定: 3086件 (Win 966 / Loss 981 / Flat 1139) / skip 2499件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $398.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.84** / 初期 $100.00 (+26.84%)
- 確定: 985件 (Win 252 / Loss 201 / Flat 532) / skip 1450件
- 成長率目線: 平均log +0.000241 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1684 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $126.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.75** / 初期 $100.00 (+0.75%)
- 確定: 226件 (Win 73 / Loss 113 / Flat 40) / pending 5件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000545 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $100.75

## 6. Latest Market Context

- 更新: 2026-07-19T11:06:08.341340+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64530.9
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +118.21% | $25,991,275.48 |
| ESPORTS/USDT:USDT | +86.39% | $49,811,958.45 |
| B/USDT:USDT | +49.54% | $39,800,696.98 |
| TLM/USDT:USDT | +48.26% | $6,132,090.11 |
| TAG/USDT:USDT | +29.88% | $4,339,426.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.10% | +4.15% |
| B/USDT:USDT | below_1h_threshold | +3.52% | +3.57% |
| TAG/USDT:USDT | below_1h_threshold | +2.30% | +2.35% |
| TLM/USDT:USDT | below_1h_threshold | +1.46% | +1.50% |
| AKE/USDT:USDT | below_1h_threshold | +1.40% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
