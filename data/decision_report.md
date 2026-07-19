# Decision Report

- generated_at: 2026-07-19T11:26:16.511954+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9026**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9026, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.68% | **+1.07%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.94% | **+0.80%** |
| LIMIT_BB3S | 4/19 | 21.1% | +2.97% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$400.28** / 初期 $100.00 (+300.28%)
- 確定: 3088件 (Win 967 / Loss 982 / Flat 1139) / skip 2499件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $400.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.27** / 初期 $100.00 (+27.27%)
- 確定: 987件 (Win 253 / Loss 202 / Flat 532) / skip 1450件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1827 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $127.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.74** / 初期 $100.00 (+0.74%)
- 確定: 228件 (Win 74 / Loss 114 / Flat 40) / pending 6件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000512 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.74

## 6. Latest Market Context

- 更新: 2026-07-19T11:26:09.331641+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64543.1
- Funnel: target 885 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +114.41% | $28,071,526.07 |
| ESPORTS/USDT:USDT | +72.01% | $50,705,966.29 |
| TLM/USDT:USDT | +57.32% | $6,453,997.67 |
| B/USDT:USDT | +48.12% | $40,460,512.38 |
| TAG/USDT:USDT | +29.15% | $4,385,094.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +2.45% | +2.47% |
| TAG/USDT:USDT | below_1h_threshold | +1.73% | +1.75% |
| HOME/USDT:USDT | below_1h_threshold | +1.35% | +1.37% |
| ZBT/USDT:USDT | below_1h_threshold | +1.14% | +1.16% |
| BASED/USDT:USDT | below_1h_threshold | +1.00% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
