# Decision Report

- generated_at: 2026-07-19T12:21:20.779281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9033**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9033, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.98% | **+1.19%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.96% | **+1.19%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.99% | **+0.90%** |
| LIMIT_2PCT | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.58% | **+1.55%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.47% | **+1.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.82** / 初期 $100.00 (+301.82%)
- 確定: 3095件 (Win 970 / Loss 985 / Flat 1140) / skip 2499件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $401.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.56** / 初期 $100.00 (+27.56%)
- 確定: 994件 (Win 256 / Loss 205 / Flat 533) / skip 1450件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1654 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $127.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.89** / 初期 $100.00 (+0.89%)
- 確定: 235件 (Win 78 / Loss 117 / Flat 40) / pending 4件 / skip 266件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000498 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.89

## 6. Latest Market Context

- 更新: 2026-07-19T12:21:10.098162+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=64357.2
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +121.76% | $33,592,212.58 |
| ESPORTS/USDT:USDT | +85.24% | $53,312,501.87 |
| TLM/USDT:USDT | +83.83% | $7,244,765.12 |
| B/USDT:USDT | +53.21% | $37,436,626.66 |
| TAG/USDT:USDT | +26.64% | $4,630,089.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +1.45% | +1.59% |
| VVV/USDT:USDT | below_1h_threshold | +0.94% | +1.08% |
| PEPE/USDT:USDT | below_1h_threshold | +0.88% | +1.01% |
| MYX/USDT:USDT | below_1h_threshold | +0.74% | +0.87% |
| LYN/USDT:USDT | below_1h_threshold | +0.70% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
