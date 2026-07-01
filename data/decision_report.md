# Decision Report

- generated_at: 2026-07-01T19:32:29.983781+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8009**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8009, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.94% | **+0.59%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.77% | **+0.48%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.01% | **+0.30%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.20% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.99% | **+0.70%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.71% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$272.37** / 初期 $100.00 (+172.37%)
- 確定: 2406件 (Win 735 / Loss 797 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NOM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $272.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.26** / 初期 $100.00 (+7.26%)
- 確定: 526件 (Win 133 / Loss 124 / Flat 269) / skip 894件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0375 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.26

## 5. Latest Market Context

- 更新: 2026-07-01T19:32:22.733095+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=60187.1
- Funnel: target 825 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +30.65% | $3,658,622.43 |
| RIF/USDT:USDT | +12.00% | $2,431,703.61 |
| AIGENSYN/USDT:USDT | +6.83% | $6,718,181.62 |
| LIT/USDT:USDT | +6.10% | $4,072,262.36 |
| VELVET/USDT:USDT | +6.06% | $27,367,726.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.49% | +4.42% |
| BEAT/USDT:USDT | below_1h_threshold | +3.60% | +3.53% |
| LIT/USDT:USDT | below_1h_threshold | +2.65% | +2.58% |
| RIF/USDT:USDT | below_1h_threshold | +2.31% | +2.24% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.18% | +2.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
